# BY Claude 3.5 
import numpy as np

def riemann_integral():
    n = 100  # 每個維度的分割數
    dx = 1.0 / n
    dy = 1.0 / n
    dz = 1.0 / n
    total = 0.0
    
    for i in range(n):
        x = (i + 0.5) * dx  # 取每個小區塊的中點
        for j in range(n):
            y = (j + 0.5) * dy
            for k in range(n):
                z = (k + 0.5) * dz
                total += (3*x*x + y*y + 2*z*z) * dx * dy * dz
                
    return total

def monte_carlo_integral(num_points=1000000):
    # 隨機生成點
    x = np.random.uniform(0, 1, num_points)
    y = np.random.uniform(0, 1, num_points)
    z = np.random.uniform(0, 1, num_points)
    
    # 計算函數值
    values = 3*x*x + y*y + 2*z*z
    
    # 計算平均值並乘以體積
    return np.mean(values) * 1.0  # 積分區域體積為 1

def main():
    print("黎曼積分結果:", riemann_integral())
    print("蒙地卡羅法結果:", monte_carlo_integral())
    
if __name__ == "__main__":
    main()

# 黎曼積分結果: 1.9999499999999708
# 蒙地卡羅法結果: 2.000523180214253
