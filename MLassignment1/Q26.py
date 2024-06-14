def check_prefix_suffix(text, prefix, suffix):
    starts_with_prefix = text.startswith(prefix)
    ends_with_suffix = text.endswith(suffix)

    if starts_with_prefix:
        print(f"The text '{text}' starts with the prefix '{prefix}'.")
    else:
        print(f"The text '{text}' does not start with the prefix '{prefix}'.")

    if ends_with_suffix:
        print(f"The text '{text}' ends with the suffix '{suffix}'.")
    else:
        print(f"The text '{text}' does not end with the suffix '{suffix}'.")


text = input("Enter a string: ")
prefix = input("Enter a prefix to check: ")
suffix = input("Enter a suffix to check: ")

check_prefix_suffix(text, prefix, suffix)


