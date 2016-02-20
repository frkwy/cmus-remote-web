import re
import subprocess
def now_playing():
	status = ""
	status_string = subprocess.check_output(["cmus-remote", '-Q'])
	for tag_name in ["title", "artist", "album"]:
		tag_value = re.search("(?<=tag\s{value}\s).*".format(value=tag_name), status_string, re.UNICODE).group(0)
		status += ("{tag_name}: {tag_value}<br>".format(tag_name=tag_name, tag_value=tag_value))
	return status	
