import requests, zipfile, io, re, os

from .archives import temp_dir

def download_zipfile(url, destination=None, overwrite=False):
	r = requests.get(url)
	if not r.ok:
		raise ValueError(r.reason)

	d = r.headers['content-disposition']
	fnames = re.findall("filename=(.+)", d)

	z = zipfile.ZipFile(io.BytesIO(r.content))
	if destination is None:
		destination = temp_dir.name

	if len(fnames):
		fname = os.path.splitext(fnames[0])[0]
		fdir = os.path.join(destination, fname)
		os.makedirs(fdir, exist_ok=True)
	else:
		fdir = destination

	z.extractall(path=fdir)
	return fdir
