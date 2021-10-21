import React from 'react';
import ReactDOM from 'react-dom';
import MediaUploader from '../helpers/media-uploader';
import { ILiveblogSettings, IProgressData, IUploadParams } from './types';
import { UploadProgress } from './uploadProgress';
import { UploadZone } from './uploadZone';

interface IProps {
    lbSettings: ILiveblogSettings;
}

interface IState {
    showProgress: boolean;
    uploadStartTime: number;
    uploadProgressData?: IProgressData;
}

class YoutubeUpload extends React.Component<IProps, IState> {
    constructor(props) {
        super(props);

        this.state = {
            showProgress: false,
            uploadStartTime: 0,
        };
    }

    uploadVideo = (params: IUploadParams) => {
        const { lbSettings } = this.props;
        const metadata = {
            snippet: {
                title: params.title,
                description: params.description,
                tags: ['youtube-cors-upload'],
                categoryId: 22,
            },
            status: {
                privacyStatus: lbSettings.youtube_privacy_status || 'unlisted',
            },
        };

        // let addContentBtns = new AddContentBtns();
        const token = localStorage.getItem('accessToken');
        let uploader = new MediaUploader({
            baseUrl: 'https://www.googleapis.com/upload/youtube/v3/videos',
            file: params.videoFile,
            token: token,
            metadata: metadata,
            params: {
                access_token: token,
            },
            onError: function(data) {
                let message = data;

                try {
                    let errorResponse = JSON.parse(data);

                    message = errorResponse.error.message;
                } finally {
                    alert(message // eslint-disable-line
                        + '\nThe direct video upload requires a connection to Youtube');

                    // self.ready();
                    // $('[data-icon="close"]').show();
                    // addContentBtns.show();
                }
            },
            onProgress: (data: IProgressData) => {
                this.setState({ uploadProgressData: data });
            },
        });

        this.setState({ uploadStartTime: Date.now(), showProgress: true });
        uploader.upload();
    }

    render() {
        const { uploadStartTime, uploadProgressData } = this.state;

        return (
            <div>
                <UploadZone uploadVideo={this.uploadVideo} />

                {this.state.showProgress ? (
                    <UploadProgress
                        uploadStartTime={uploadStartTime}
                        progressData={uploadProgressData}
                    />
                ) :
                    null}
            </div>
        );
    }
}

export const renderYoutubeUpload = (mountPoint: HTMLElement, props: IProps) => {
    ReactDOM.render(<YoutubeUpload {...props} />, mountPoint);
};