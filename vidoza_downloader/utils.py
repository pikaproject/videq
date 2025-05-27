import re
import os

def sanitize_filename(filename: str) -> str:
    """
    Membersihkan nama file dari karakter yang tidak valid untuk sistem file.
    Juga membatasi panjang nama file untuk menghindari masalah path.

    Args:
        filename (str): Nama file asli.

    Returns:
        str: Nama file yang sudah dibersihkan.
    """
    if not filename:
        return "video_tanpa_judul"
    
    sanitized = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '', filename)

    sanitized = re.sub(r'\s+', ' ', sanitized).strip()

    max_len = 200
    if len(sanitized) > max_len:
        name, ext = os.path.splitext(sanitized)
        name = name[:max_len - len(ext)]
        sanitized = name + ext
    
    if not sanitized:
        return "video_tanpa_judul"
    
    return sanitized