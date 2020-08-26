import pymongo
from bson.objectid import ObjectId
from superdesk import get_resource_service
from html5lib.html5parser import ParseError
from lxml.html.html5parser import fragments_fromstring, HTMLParser

from liveblog.posts.mixins import AuthorsMixin
from liveblog.posts.utils import get_associations


def is_valid_html(html):
    try:
        fragments_fromstring(html.encode('utf-8'), parser=HTMLParser(strict=True))
    except ParseError:
        return False
    return True


class Blog(AuthorsMixin):
    """
    Utility class to fetch blog data directly from mongo collections.
    """

    order_by = ('_updated', '_created', 'order')
    sort = ('asc', 'desc')
    ordering = {
        'newest_first': ('_created', 'desc'),
        'oldest_first': ('_created', 'asc'),
        'editorial': ('order', 'desc')
    }
    default_ordering = 'newest_first'
    default_order_by = '_created'
    default_sort = 'desc'
    default_page = 1
    default_page_limit = 25
    max_page_limit = 100

    def __init__(self, blog):
        if isinstance(blog, (str, ObjectId)):
            blog = get_resource_service('client_blogs').find_one(_id=blog, req=None)

        self._blog = blog
        self._posts_service = get_resource_service('client_blog_posts')

    def _posts_lookup(self, sticky=None, highlight=None, all_posts=False, deleted=False, tags=[]):
        filters = [
            {'blog': self._blog['_id']}
        ]

        # only return all post if parameter is specified. Otherwise
        # get only open posts and not deleted
        if not all_posts:
            filters.append({'post_status': 'open'})
            if not deleted:
                filters.append({'deleted': False})

        if sticky:
            filters.append({'sticky': True})
        else:
            filters.append({'sticky': False})

        if highlight:
            filters.append({'lb_highlight': True})

        if len(tags) > 0:
            filters.append({'tags': {'$in': tags}})

        return {'$and': filters}

    def get_ordering(self, label):
        try:
            order_by, sort = self.ordering[label]
            return order_by, sort
        except KeyError:
            return self.default_order_by, self.default_sort

    def check_html_markup(self, original_text):
        div_wrapped = '<div>{}</div>'.format(original_text)
        if not is_valid_html(original_text) and is_valid_html(div_wrapped):
            original_text = div_wrapped
        return original_text

    def posts(self, **kwargs):
        """
        Builds a query with the given parameters and hit mongodb to retrive the data
        Uses `find` method from resource service. If wrap parameter is provided, the return
        value it's a dictionary ala `python-eve` style data structure

        Supported kwargs: sticky, highlight, ordering, page, limit, wrap, all_posts, deleted, tags

        TODO: restrict parameters to only allowed ones
        """

        sticky = kwargs.get('sticky', None)
        highlight = kwargs.get('highlight', None)
        ordering = kwargs.get('ordering', None)
        page = kwargs.get('page', self.default_page)
        limit = kwargs.get('limit', self.default_page_limit)
        wrap = kwargs.get('wrap', False)
        all_posts = kwargs.get('all_posts', False)
        deleted = kwargs.get('deleted', False)
        tags = kwargs.get('tags', [])

        order_by, sort = self.get_ordering(ordering or self.default_ordering)
        lookup = self._posts_lookup(sticky, highlight, all_posts, deleted, tags)
        results = self._posts_service.find(lookup)
        total = results.count()

        # Get sorting direction.
        sort = pymongo.DESCENDING
        if sort == 'asc':
            sort = pymongo.ASCENDING

        # Fetch posts, do pagination and sorting.
        skip = limit * (page - 1)
        results = results.skip(skip).limit(limit).sort(order_by, sort)

        posts = [x for x in results if 'groups' in x]
        related_items = self._posts_service._related_items_map(posts)

        for post in posts:
            for assoc in get_associations(post):
                ref_id = assoc.get('residRef', None)
                if ref_id:
                    assoc['item'] = related_items[ref_id]
                    original_text = assoc['item'].get('text')
                    assoc['item']['text'] = self.check_html_markup(original_text)

        # Enrich documents
        self.complete_posts_info(posts)

        if wrap:
            # Wrap in python-eve style data structure
            return {
                '_items': posts,
                '_meta': {
                    'page': page,
                    'total': total,
                    'max_results': limit
                }
            }

        return posts
