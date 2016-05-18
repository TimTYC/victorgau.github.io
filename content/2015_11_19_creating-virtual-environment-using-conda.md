Title: Creating Virtual Environment Using Conda
Date: 2015-11-19 17:07
Tags: Python, Conda
Category: Python
Slug: creating-virtual-environment-using-conda
Summary: Creating Virtual Environments Using Conda

```Python
# 檢查 conda 的版本
conda -V

# 更新 conda
conda update conda

# 建立 virtual environment
conda create -n yourenvname python=x.x anaconda

# 列出所有 virtual environment
conda info -e

# 啟動 virtual environment
source activate yourenvname

# 安裝 package (我覺得使用 pip 好像比較簡單！)
conda install -n yourenvname [package]

# 注意：如果沒有加 "-n yourenvname"，則套件會被安裝到 root env

# 停止 virtual environment
source deactivate

# 刪除 virtual environment
conda remove -n yourenvname -all
```

Reference:

* [Create virtual environments for python with conda](http://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/)