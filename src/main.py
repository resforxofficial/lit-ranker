import json

def analyzeLit(fp: str):
    with open(fp, "r", encoding="utf-8") as f:
        try:
            content = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError("파일을 찾을수 없습니다")
        except Exception as e:
            raise Exception(e)

    sorted_data = sorted(content, key=lambda x: x["count"], reverse=True)

# 2. 정렬된 결과를 텍스트 파일에 저장
    with open("../dist/res.txt", "w", encoding="utf-8") as f:
        for rank, entry in enumerate(sorted_data, start=1):
            if rank > 100:
                break

            user_info = entry["userInfos"][0]  # `userInfos`에서 첫 번째 요소 선택
            f.write(f"{rank}:{user_info}\n")
