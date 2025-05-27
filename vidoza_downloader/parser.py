import re
from typing import Dict, Optional, Any
from bs4 import BeautifulSoup

def parse_video_info(html_content: str) -> Optional[Dict[str, Any]]:
    """
    Mengekstrak informasi video dari halaman unduhan.
    Mengembalikan kamus berisi judul, durasi, ukuran, dan tanggal unggah.
    """
    try:
        soup = BeautifulSoup(html_content, 'html.parser')

        title_element = soup.find('h4')
        duration_element = soup.find('div', class_='length')
        size_element = soup.find('div', class_='size')
        upload_date_element = soup.find('div', class_='uploadate')

        info  = {
            'title': title_element.text.strip() if title_element else None,
            'duration': duration_element.text.strip() if duration_element else None,
            'size': size_element.text.strip() if size_element else None,
            'upload_date': upload_date_element.text.strip() if upload_date_element else None,
        }

        if not info['title']:
            return None

        return info
    except Exception as e:
        return None

def extract_video_id(html_content: str) -> Optional[str]:
    """
    Mengekstrak video ID dari konten HTML menggunakan regular expression.
    """
    match = re.search(r"var\s+id\s*=\s*'([^']+)'", html_content)
    if match:
        return match.group(1)
    return None

def extract_object_key(html_content: str) -> Optional[str]:
    """
    Mengekstrak object key dari konten HTML halaman embed.
    """
    match = re.search(r'objectKey:\s*"([^"]+)"', html_content)
    if match:
        return match.group(1)
    return None