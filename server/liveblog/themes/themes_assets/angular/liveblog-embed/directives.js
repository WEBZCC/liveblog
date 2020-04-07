const COOKIE_NAME = '__lb_consent_cookie__';
const COOKIE_LIFE_DAYS = 365;
const CONSENT_ACCEPT_SELECTOR = '.lb_consent--accept';

(function(angular) {
    'use strict';
    angular.module('liveblog-embed')
        .directive('lbBindHtml', [function() {
            return {
                restrict: 'A',
                link: function(scope, elem, attrs) {
                    attrs.$observe('htmlContent', function() {
                        if (attrs.htmlLocation) {
                            //need to inject the html in a specific element
                            elem.find('[' + attrs.htmlLocation + ']').html(attrs.htmlContent);
                        } else {
                            //inject streaght in the elem
                            elem.html(attrs.htmlContent);
                        }
                    });
                }
            };
        }])
        /**
         * Save the aspect ratio of the orignal iframe, set the full width and preserve the original ratio
         */
        .directive('lbFluidIframe', ['$timeout', '$window', function($timeout, $window) {
            return {
                restrict: 'EA',
                link: function(scope, elem, attrs) {
                    var iframe;
                    $timeout(function() {
                        iframe = elem.find('iframe');
                        iframe.data('aspectRatio', iframe.attr('height') / iframe.attr('width'));
                        resize();
                    }, 1000);
                    function resize() {
                        var newWidth = elem.innerWidth();
                        if (newWidth < iframe.attr('width')) {
                            iframe
                                .width(newWidth)
                                .height(newWidth * iframe.data('aspectRatio'));
                        }

                    }
                    angular.element($window).bind('resize', _.debounce(resize, 1000));
                }
            };
        }])
        .directive('lbGdprEmbedConsent', [
            'config', 'asset', 'cookies', '$timeout',
            function(config, asset, cookies, $timeout) {
                return {
                    template: '<ng-include src="getTemplateUrl()" />',
                    scope: {
                        item: '=',
                        timeline: '='
                    },
                    restrict: 'E',
                    link: function(scope, elem, attrs) {
                        $timeout(function () {
                            var acceptButton = angular.element(elem).find(CONSENT_ACCEPT_SELECTOR);
                            acceptButton.on('click', function(ev) {
                                ev.preventDefault();

                                cookies.write(COOKIE_NAME, 'Y', COOKIE_LIFE_DAYS);
                            });
                        });
                    },
                    controller: ['$scope', function($scope) {
                        var consentIsGiven = function() {
                            return cookies.read(COOKIE_NAME) === 'Y';
                        };

                        var domainRequiresConsent = function(providerUrl) {
                            if (!providerUrl)
                                return false;

                            var domains = config.settings.gdprConsentDomains;

                            if (domains.length > 0) {
                                // get domains and remove possible blank spaces
                                domains = domains.split(',');
                                domains = domains.map(function(x) {return x.trim().toLowerCase()});

                                var embedDomain = new URL(providerUrl).hostname;
                                embedDomain = embedDomain.replace('www.', '');

                                return domains.indexOf(embedDomain) !== -1;
                            }

                            return false;
                        };

                        // used on the ng-include to resolve the template
                        $scope.getTemplateUrl = function() {
                            var item = $scope.item;
                            var templateName;

                            if (config.settings.enableGdprConsent) {
                                const providerUrl = item.meta.provider_url;

                                if (!consentIsGiven() && domainRequiresConsent(providerUrl)) {
                                    return asset.templateUrl("views/embeds/consent-placeholder.html");
                                }
                            }

                            switch (item.meta.provider_name) {
                                case "Twitter":
                                case "Facebook":
                                case "Instagram":
                                    templateName = "views/embeds/" + item.meta.provider_name.toLowerCase() + ".html";
                                    break;
                                default:
                                    templateName = "views/embeds/generic.html";
                                    break;
                            }

                            return asset.templateUrl(templateName);
                        }
                    }]
                }
            }
        ])
        .directive('lbTwitterCard', [function() {
            return {
                restrict: 'E',
                link: function(scope, elem, attrs) {
                    elem.html(attrs.lbTwitterContent);
                }
            };
        }])
        .directive('lbGenericEmbed', ['$timeout', '$window', 'asset', function($timeout, $window, asset) {
            return {
                scope: {
                    item: '='
                },
                templateUrl: asset.templateUrl('views/generic-embed.html')
            };
        }])
        .directive("lbDropdown", ['$rootScope', 'asset', function($rootScope, asset) {
                return {
                    restrict: "E",
                    templateUrl: asset.templateUrl('views/dropdown.html'),
                    scope: {
                        placeholder: "@",
                        list: "=",
                        selected: "&",
                        order: "&"
                    },
                    link: function(scope) {
                        scope.listVisible = false;
                        scope.isPlaceholder = true;

                        scope.select = function(item) {
                            scope.isPlaceholder = false;
                            scope.order({order: item.order});
                            scope.listVisible = false;
                        };

                        scope.isSelected = function(item) {
                            return item.order === scope.selected();
                        };

                        scope.show = function() {
                            scope.listVisible = true;
                        };

                        $rootScope.$on("documentClicked", function(inner, target) {
                            if ($(target[0]).parents(".dropdown-display").length == 0 || $(target[0]).parents(".dropdown-display.clicked").length > 0) {
                                scope.$apply(function() {
                                    scope.listVisible = false;
                                });
                            }
                        });

                        scope.$watch("selected()", function(value) {
                            _.each(scope.list, function(item) {
                                if(item.order === scope.selected()) {
                                    scope.display = item.name;
                                    scope.isPlaceholder = false;
                                }
                            });
                        });
                    }
                }
            }]);
        ;
})(angular);
