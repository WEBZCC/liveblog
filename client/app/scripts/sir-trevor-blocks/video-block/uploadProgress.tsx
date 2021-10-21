import React from 'react';
import { IProgressData } from './types';

interface IProps {
    progressData: IProgressData;
    uploadStartTime: number;
}

export class UploadProgress extends React.Component<IProps> {
    calculateProgress = (data: IProgressData) => {
        const currentTime = Date.now();
        const bytesUploaded = data.loaded;
        const totalBytes = data.total;

        // Time is in ms, so we need to convert them to seconds
        const bytesPerSecond = bytesUploaded / ((currentTime - this.props.uploadStartTime) / 1000);
        const estimatedSecondsRemaining = ((totalBytes - bytesUploaded) / bytesPerSecond).toFixed(2);
        const percentageComplete = ((bytesUploaded * 100) / totalBytes).toFixed(2);

        return {
            percentageComplete,
            estimatedSecondsRemaining,
        };
    }


    render() {
        const data = this.props.progressData;
        const progress = this.calculateProgress(data);
        const bytesUploaded = data.loaded;
        const totalBytes = data.total;

        return (
            <div>
                <div className="upload-status">
                    Please wait until the upload completes. Do not close or reload your browser.
                </div>
                <br />
                <div className="remaining-time">
                    {`Time Left: ${progress.estimatedSecondsRemaining} Seconds`}
                </div>
                <br />
                <div className="during-upload">
                    <p>
                        <span>{progress.percentageComplete}</span>
                        % Done (<span>{bytesUploaded}</span> <span>{totalBytes}</span>)
                    </p>
                    <progress max={totalBytes} value={bytesUploaded} />
                </div>
            </div>
        );
    }
}