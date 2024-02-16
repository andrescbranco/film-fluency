import React, { useRef } from 'react';

const VideoPlayer = ({ src }) => {
    const videoRef = useRef(null);

    const handlePlayVideo = () => {
        videoRef.current.play();
    };

    const handlePauseVideo = () => {
        videoRef.current.pause();
    };

    return (
        <div>
            <div className='video-player-frame'>
            <video className='video' ref={videoRef} controls>
                <source src={src} type="video/mp4" />
                Your browser does not support the video tag.
            </video>
            </div>
        </div>
    );
};

export default VideoPlayer;