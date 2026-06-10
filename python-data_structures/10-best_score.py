cat << 'EOF' > 10-best_score.py
#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
EOF
chmod +x 10-best_score.py
