import subprocess
import os

def lip_sync(video_path, audio_path, output_path, wav2lip_repo_path='externals/Wav2Lip'):
    """
    Runs Wav2Lip inference to lip sync video path with audio path; saves 
    output to output_path

    Args:
        video_path (str): path to video
        audio_path (str): path to .wav audio with cloned voice
        output_path (str): path where the synced video will be saved
    """

    checkpoint_path = os.path.join(wav2lip_repo_path, "checkpoints", "wav2lip_gan.pth")

    command = ["python", os.path.join(wav2lip_repo_path, "inference.py"), 
               "--checkpoint_path", checkpoint_path,
               "--face", video_path,
               "--audio", audio_path,
               "--outfile", output_path 
               ]
    
    print(f"Running Wav2Lip inference.py")

    result = subprocess.run(command, capture_output=True, text=True)

    # messgaes to print if inference fails or completes
    if result.returncode != 0:
        print("Wav2Lip error output:\n", result.stderr)
        raise RuntimeError("Wav2Lip inference failed")
    else:
        print("Wav2Lip finished successfully.")
        print(result.stdout)