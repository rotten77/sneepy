DEL sneepy.ico
RMDIR "TMP" /s /q
MKDIR "TMP"
"C:\Program Files\Inkscape\bin\inkscape.exe" -w 16 -h 16 sneepy-icon.svg -o TMP/ico-16.png
"C:\Program Files\Inkscape\bin\inkscape.exe" -w 32 -h 32 sneepy-icon.svg -o TMP/ico-32.png
"C:\Program Files\Inkscape\bin\inkscape.exe" -w 48 -h 48 sneepy-icon.svg -o TMP/ico-48.png
"C:\Program Files\Inkscape\bin\inkscape.exe" -w 128 -h 128 sneepy-icon.svg -o TMP/ico-128.png
"C:\Program Files\Inkscape\bin\inkscape.exe" -w 256 -h 256 sneepy-icon.svg -o TMP/ico-256.png

magick.exe TMP/ico-16.png TMP/ico-32.png TMP/ico-48.png TMP/ico-128.png TMP/ico-256.png sneepy.ico

RMDIR "TMP" /s /q