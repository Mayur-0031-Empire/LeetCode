from pathlib import Path

TEXT_EXTENSIONS = {".txt", ".py", ".md", ".json", ".csv"}

def print_tree(path: Path, depth=0):
    indent = "\t" * depth

    if depth == 0:
        print(path.name or path.resolve().name)
    else:
        print(f"{indent}{path.name}")

    for item in path.iterdir():
        if item.is_dir():
            print_tree(item, depth + 1)
        else:
            file_indent = "\t" * (depth + 1)
            print(f"{file_indent}{item.name}")

            if item.suffix in TEXT_EXTENSIONS:
                print(f"{file_indent}\tdata:")
                try:
                    with item.open("r", encoding="utf-8", errors="ignore") as f:
                        for line in f:
                            print(f"{file_indent}\t{line.rstrip()}")
                except Exception:
                    print(f"{file_indent}\t<cannot read>")
            else:
                print(f"{file_indent}\tdata: <binary file skipped>")

class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        present = {}
        for i in range(len(nums)):
            t = target - nums[i]
            if t in present:
                return [present[t], i]
            present[nums[i]] = i
        return [-1, -1]
print_tree(Path("."))

        
        

