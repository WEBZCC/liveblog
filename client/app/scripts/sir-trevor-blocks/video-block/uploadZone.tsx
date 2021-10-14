import React from 'react';
import ReactDOM from 'react-dom';
import { VideoPreview } from './videoPreview';

interface IProps {

}

interface IState {
    videoFile: File;
}

class UploadZone extends React.Component<IProps, IState> {
    videoInput: HTMLInputElement;
    uploadButton: HTMLButtonElement;

    constructor(props) {
        super(props);

        this.state = { videoFile: null };
    }

    onVideoChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const files = e.target.files;

        if (files.length > 0)
            this.setState({ videoFile: files[0] });
    }

    componentDidMount = () => {
        // NOTE: Wondering why I wired the click event that way?
        // Well, the dang SirTrevor SimpleBlock code has a bind with stopPropagation
        // therefore it's eating React onClick events bind for some reason
        $(this.uploadButton).on('click', () => $(this.videoInput).trigger('click'));
    }

    render() {
        return (
            <div className="row st-block__upload-container">
                <div className="col-12">
                    <button
                        ref={(e) => this.uploadButton = e}
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
                </div>
            </div>
        );
    }
}

export const renderUploadZone = (mountPoint: HTMLElement) => {
    ReactDOM.render(<UploadZone />, mountPoint);
};
