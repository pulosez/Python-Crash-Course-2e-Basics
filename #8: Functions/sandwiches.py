# 8.12.
def make_sandwich(*items):
    print(f"\nMaking a sandwich with the followig items:")
    for item in items:
        print(f"- {item}")

make_sandwich('chicken', 'egg')
make_sandwich('fish')
make_sandwich('cheese', 'chicken', 'olives')
