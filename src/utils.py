import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(path):
    """Load dataset dari file CSV."""
    return pd.read_csv(path)

def save_data(df, path):
    """Simpan DataFrame ke file CSV."""
    df.to_csv(path, index=False)

def plot_top_products_by_industry(df, top_n=3):
    """
    Visualisasi produk terlaris per industri.
    """
    grouped = df.groupby(['Industry', 'Product']).size().reset_index(name='Order Count')
    top_products = grouped.groupby('Industry').apply(lambda x: x.nlargest(top_n, 'Order Count')).reset_index(drop=True)
    
    plt.figure(figsize=(12, 6))
    sns.barplot(data=top_products, x='Industry', y='Order Count', hue='Product')
    plt.title(f'Top {top_n} Products per Industry')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def detect_outliers_iqr(df, column):
    """
    Deteksi outlier menggunakan metode IQR.
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] < lower_bound) | (df[column] > upper_bound)]

def summary_statistics(df):
    """
    Menampilkan ringkasan statistik dari DataFrame.
    """
    return df.describe()

def boxplot_column(df, column):
    """
    Tampilkan boxplot dari kolom numerik.
    """
    plt.figure(figsize=(6, 4))
    sns.boxplot(y=df[column])
    plt.title(f'Boxplot of {column}')
    plt.tight_layout()
    plt.show()
