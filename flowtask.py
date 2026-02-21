import random
import sys
def main():
    print("==============================")
    print("   FlowTask MVP 起動成功！")
    print("==============================")
    tasks = ["🧠 企画を練る", "💻 コードを書く", "🧹 デスクを片付ける", "📝 ドキュメント作成"]
    if len(sys.argv) > 1 and sys.argv[1] == "random":
        print(f"【抽選結果】今日のタスクは... >> {random.choice(tasks)} << です！")
    else:
        print("利用可能なタスク一覧:")
        for t in tasks:
            print(f" - {t}")
        print("\n使い方: python flowtask.py random で抽選できます")
if __name__ == '__main__':
    main()