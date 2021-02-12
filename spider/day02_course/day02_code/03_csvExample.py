"""
    csv模块使用
"""
import csv

with open('fengyun.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['聂风', '雪饮狂刀'])
    writer.writerow(['步惊云', '绝世好剑'])
    writer.writerow(['雄霸', '三分归元气'])





















