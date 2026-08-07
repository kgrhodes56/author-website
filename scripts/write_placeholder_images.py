import os, base64

images = {
    'dale-gatekeeper-guardian.png': 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGNgYAAAAAMAAWgmWQ0AAAAASUVORK5CYII=',
    'ezra-the-anchor.png': 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGNgYAAAAAMAAWgmWQ0AAAAASUVORK5CYII=',
    'astrid-healer-telekinetic.png': 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGNgYAAAAAMAAWgmWQ0AAAAASUVORK5CYII=',
    'rain-seer-teleporter.png': 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGNgYAAAAAMAAWgmWQ0AAAAASUVORK5CYII='
}

out_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'images')
os.makedirs(out_dir, exist_ok=True)
for name, b64 in images.items():
    path = os.path.join(out_dir, name)
    with open(path, 'wb') as f:
        f.write(base64.b64decode(b64))
print('Wrote', len(images), 'placeholder images to', out_dir)
