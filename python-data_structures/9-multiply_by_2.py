cat << 'EOF' > 9-multiply_by_2.py
#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return {key: val * 2 for key, val in a_dictionary.items()}
EOF
chmod +x 9-multiply_by_2.py
