import os
from lotus.wp import WordPressXMLWriter

# WordPress blog title
title = "My Logbook"

# archive directory
archive_dir = "/path/to/converted/xml/files"

# path to store WordPress XML file
wp_file = os.path.join(archive_dir, "wp.xml")

# blog site ID (get this from the WordPress network admin sites screen)
site_id = 22

# URL for main network site (the default site for a WordPress network installation),
# with trailing slash
base_network_url = "https://test.some-site.com/"

# URL for blog (with trailing slash)
base_url = base_network_url + "tmp3/"

# URL for directory containing all source media generated from LotusXMLBuilder
# (WordPress will sideload media from this directory)
# This can be any web-accessible directory
base_source_media_url = "https://example.com/path/to/media/"

# Path to write logs to. Set to None for no logs.
debug_log_file = "wp.log"

if __name__ == "__main__":
    writer = WordPressXMLWriter(title, archive_dir, wp_file, site_id, base_network_url, base_url,
                                base_source_media_url, debug_log_file=debug_log_file)
    writer.generate()