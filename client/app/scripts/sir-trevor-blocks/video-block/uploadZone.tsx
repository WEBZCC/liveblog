import React from 'react';
import { VideoPreview } from './videoPreview';

interface IUploadParams {
    title: string;
    description: string;
    videoFile: File;
}

interface IProps {
    uploadVideo: (params: IUploadParams) => void;
}

interface IState {
    videoFile: File;
}

export class UploadZone extends React.Component<IProps, IState> {
    videoInput: HTMLInputElement;
    pickFileButton: HTMLButtonElement;
    uploadButton: HTMLButtonElement;

    title: HTMLDivElement;
    description: HTMLDivElement;

    constructor(props) {
        super(props);

        this.state = { videoFile: null };
    }

    onVideoChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const files = e.target.files;

        if (files.length > 0)
            this.setState({ videoFile: files[0] });
    }

    onUploadToYoutubeClicked = () => {
        const params: IUploadParams = {
            title: $(this.title).text(),
            description: $(this.description).text(),
            videoFile: this.state.videoFile,
        };

        this.props.uploadVideo(params);
    }

    componentDidMount = () => {
        // NOTE: Wondering why I wired the click event that way?
        // Well, the dang SirTrevor SimpleBlock code has a bind with stopPropagation
        // therefore it's eating React onClick events bind for some reason
        $(this.pickFileButton).on('click', () => $(this.videoInput).trigger('click'));
        $(this.uploadButton).on('click', this.onUploadToYoutubeClicked);
    }

    render() {
        return (
            <div className="row st-block__upload-container">
                <div className="col-12">
                    <button
                        ref={(e) => this.pickFileButton = e}
                        className="btn btn-default"
                        type="button"
                    >
                        Select from folder
                    </button>
                    <input
                        type="file"
                        ref={(e) => this.videoInput = e}
                        onChange={this.onVideoChange}
                    />

                    <VideoPreview videoFile={this.state.videoFile} />

                    <div className="item--embed__info">
                        <div
                            className="st-embed-block item--embed__title title-preview"
                            contentEditable={true}
                            placeholder="Add a title"
                            ref={(el) => this.title = el}
                        />

                        <div
                            className="st-embed-block item--embed__description description-preview"
                            contentEditable={true}
                            placeholder="Add a description"
                            ref={(el) => this.description = el}
                        />
                    </div>

                    <button
                        disabled={!this.state.videoFile}
                        ref={(el) => this.uploadButton = el}
                        type="button"
                        className="btn btn--primary pull-right"
                    >
                        Upload to Youtube
                    </button>
                </div>
            </div>
        );
    }
}
