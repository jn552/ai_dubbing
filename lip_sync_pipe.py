import sys
import os
from lip_sync import lip_sync
from reduce_vid_quality import reduce_video_quality

def main():

    if len(sys.argv) < 3:
        print("Usage: python pipeline.py <audio> <video>")
        sys.exit(1)

    audio_file = sys.argv[1]
    video_file = sys.argv[2]

    # checking file existence
    if not os.path.exists(audio_file):
        print(f"Audio/Video file {audio_file} not found.")
        sys.exit(1)

    if not os.path.exists(video_file):
        print(f"Audio/Video file {video_file} not found.")
        sys.exit(1)

    base_output_dir = "outputs"
    base_name = os.path.splitext(os.path.basename(video_file))[0]
    output_dir = os.path.join(base_output_dir, base_name)
    os.makedirs(output_dir, exist_ok=True)

    # reduce video quality to reduce RAM usage
    reduced_video_file = reduce_video_quality(video_file, os.path.join(output_dir, f"{base_name}.reduced.MOV") )

    # generating video with synced lips 
    lip_sync(reduced_video_file, audio_file, os.path.join(output_dir, f"{base_name}.dubbed.mp4"))
    

if __name__ == "__main__":
    main()