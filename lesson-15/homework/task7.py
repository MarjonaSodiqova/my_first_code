import matplotlib.pyplot as plt

products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]
colors = ['skyblue', 'salmon', 'lightgreen', 'gold', 'orchid']

plt.figure(figsize=(8, 6))
plt.bar(products, sales, color=colors, edgecolor='black', width=0.6)

plt.title('Product Sales Performance', fontsize=14, pad=20)
plt.xlabel('Products', fontsize=12)
plt.ylabel('Sales (units)', fontsize=12)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.ylim(0, 300)

plt.show()