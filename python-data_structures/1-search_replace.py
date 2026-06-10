cat << 'EOF' > 1-search_replace.py
#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if x == search else x for x in my_list]
EOF
chmod +x 1-search_replace.py
