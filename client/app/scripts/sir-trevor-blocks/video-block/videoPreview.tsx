import React from 'react';

interface IProps {
    videoFile: File;
}

export const VideoPreview: React.FunctionComponent<IProps> = (props) => {
    if (!props.videoFile)
        return null;

    const videoUrl = URL.createObjectURL(props.videoFile);
    const name = props.videoFile.name;

    return (
        <div className="video-preview">
            <p>{name}</p>
            <video src={videoUrl} />
        </div>
    );
};
