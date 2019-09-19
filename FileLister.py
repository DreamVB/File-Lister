import glob
import sys

# Open html include file
f = open("inc\\html.inc","r")
# Check file mode
if f.mode == "r":
    # Read the contents of file into header
    header = f.read()
# Close file
f.close()

footer = """	</body>
</html>"""

if len(sys.argv) == 1:
    print("Folder path is required.")
    exit(1)

# Get the path that we will be scaning
scan_path = sys.argv[1]
# Extract scan folder path
lz_path = scan_path[0:scan_path.rindex("\\") + 1]

# Set buffer to html include data
strbuff = header
# Add page header
strbuff += "<h1>File Listing of<span>" + lz_path + "</span></h1>\n"
# Add tag for unsorted list
strbuff += "<ul>\n"

# Get a list of files.
results = glob.glob(scan_path)
# Check that files were found
if len(results) == 0:
    print("Not files were found in the selected path.")
    exit(1)
# Print files
for file in results:
    # Extract filename
    lz_file = file[file.rindex("\\") + 1:]
    # Add html list tag to final data
    strbuff += "<li><a href=" + lz_file + ">" + lz_file + "</a></li>\n"
# Add  html ending tags for unordered list
strbuff += "<ul></div>\n"
# Add html footer
strbuff += footer
# Push the data to the user
print(strbuff)
