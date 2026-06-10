cat << 'EOF' > 4-only_diff_elements.py
#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return set_1 ^ set_2
EOF
chmod +x 4-only_diff_elements.py
