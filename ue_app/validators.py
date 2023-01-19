import os
import magic
from django.core.exceptions import ValidationError


def validate_is_audio(file):
    valid_mime_types = ['audio/basic', 'auido/L24',
                        'audio/mid', 'audio/mpeg', 'audio/mp4', 'audio/x-aiff', 'audio/x-mpegurl', 'audio/vnd.rn-realaudio', 'audio/ogg', 'audio/vorbis', 'audio/vnd.wav']
    file_mime_type = magic.from_buffer(file.read(2024), mime=True)
    if file_mime_type not in valid_mime_types:
        raise ValidationError('Unsupported file type.')
    valid_file_extensions = ['.mp3', '.wav', '.vorbis', '.ogg', '.mp4', '.ram', '.ra', '.aiff', '.aif','.aifc','.rmi', '.mid', '.au','.snd']
    ext = os.path.splitext(file.name)[1]
    if ext.lower() not in valid_file_extensions:
        raise ValidationError('Unacceptable file extension.')


def validate_is_video(file):
    valid_mime_types = ['video/x-flv', 'video/mp4',
                        'application/x-mpegURL', 'video/MP2T', 'video/3gpp', 'video/quicktime', 'video/x-msvideo', 'video/x-ms-wmv',]
    file_mime_type = magic.from_buffer(file.read(1024), mime=True)
    if file_mime_type not in valid_mime_types:
        raise ValidationError('Unsupported file type.')
    valid_file_extensions = ['.flv', '.mp4', '.m3u8', '.ts', '.3gp',
                             '.mov', '.avi', '.wmv',]
    ext = os.path.splitext(file.name)[1]
    if ext.lower() not in valid_file_extensions:
        raise ValidationError('Unacceptable file extension.')
