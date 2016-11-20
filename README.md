## OpenCVでアニメ顔画像データセット作成

このコードはOpenCVでアニメ画像から顔領域を切り出し、指定のサイズにリサイズして顔画像データセットを構築することができます。

## 使い方

### 事前準備

[lbpcascade_animeface.xml](https://github.com/nagadomi/lbpcascade_animeface)を`run.py`と同じ階層に入れていおきます。

### 元画像の配置

画像が入っているフォルダ群が入っているフォルダをsource_dirとします。

```
source_dir
├── sub_dir_0
│   ├── image_0.png
│   │   ... 
│   └── image_12345.py
├── sub_dir_1
│   ├── image_0.png
│   │   ... 
│   └── image_12345.py
```

## 実行

`python run.py --source_dir SOURCE_DIR --output_dir OUTPUT_DIR --size IMAGE_SIZE`