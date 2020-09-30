import modalHtml from './ui/shared-post-modal.html';

const modalUrl = 'https://unpkg.com/micromodal@0.4.6/dist/micromodal.min.js';

const modalScriptReady = () => {
    const MicroModal = (window as any).MicroModal;

    MicroModal.show('lb--shared-post-modal');
};

export const handleSharedPost = (postId: string) => {
    // step 1: include modal library (js, modal html and css)
    document.body.insertAdjacentHTML('beforeend', modalHtml);

    const mScript = document.createElement('script');

    mScript.type = 'text/javascript';
    mScript.src = modalUrl;
    mScript.async = true;
    mScript.defer = true;
    mScript.onload = modalScriptReady;
    document.body.appendChild(mScript);

    // step 2: fetch post from backend
    // step 3: render things
    console.log(postId); // eslint-disable-line
};