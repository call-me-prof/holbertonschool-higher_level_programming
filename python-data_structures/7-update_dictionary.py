cat << 'EOF' > 7-update_dictionary.py
#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary
EOF
chmod +x 7-update_dictionary.py
