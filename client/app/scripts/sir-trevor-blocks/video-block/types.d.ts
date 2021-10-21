export interface IUploadParams {
    title: string;
    description: string;
    videoFile: File;
}

export interface ILiveblogSettings {
    youtube_privacy_status: string;
}

export interface IProgressData {
    loaded: number;
    total: number;
}
