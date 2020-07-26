# sk-surprise 库默认的movie 数据集
from surprise import KNNWithMeans
from surprise import Dataset
from surprise import evaluate, print_perf
from surprise import model_selection

# 默认载入movielens数据集
data = Dataset.load_builtin('ml-100k')
# k折交叉验证(k=3)
data.split(n_folds=3)
# 试一把SVD矩阵分解
algo = KNNWithMeans()
# 在数据集上测试一下效果  交叉验证
perf = evaluate(algo, data, measures=['RMSE', 'MAE'])


#推荐另一个函数？model_selection.cross_ validate   这里是拆分成了五折
# pref=model_selection.cross_validate(algo,measures=['RMSE','MAE'])

#输出结果
print_perf(perf)