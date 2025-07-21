# カメラデータベース

研究やアプリケーション開発のためのオープンソースのカメラ仕様と画像データベース。

## 概要

このリポジトリには、さまざまなメーカーの3,586台のデジタルカメラの詳細な仕様と、カメラ画像のサンプルが含まれています。完全なデータセットには3,585枚のカメラ画像が含まれています。

> **注意**：GitHubのファイルサイズ制限により、このリポジトリにはカメラ画像の一部のみが含まれています。完全な画像データセットはリクエストに応じて提供可能です。




## リポジトリの構造

```
CameraDatabase/
├── data/                          # データディレクトリ
│   ├── camera_data.csv    # CSV形式のカメラ仕様
│   ├── camera_data.json   # JSON形式のカメラ仕様
│   └── images/                    # カメラ画像サンプル
├── doc/                           # ドキュメントディレクトリ
│   ├── README_en.md               # 英語ドキュメント
│   ├── README_zh.md               # 中国語ドキュメント
│   ├── README_ja.md               # 日本語ドキュメント （本ファイル）
│   ├── README_es.md               # スペイン語ドキュメント
│   ├── README_fr.md               # フランス語ドキュメント
│   └── README_de.md               # ドイツ語ドキュメント
└── README.md                      # メインREADMEファイル
```




## データファイル

- `data/camera_data.csv`: CSV形式のカメラ仕様データ（37列）
- `data/camera_data.json`: JSON形式のカメラ仕様データ（CSVと同じデータ）
- `data/images/`: カメラ画像サンプル（PNG形式）のディレクトリ

## データ構造

データセットには以下のフィールドが含まれています：

| 英語フィールド | 日本語訳 | 説明 |
|---------|----------|------|
| Brand | ブランド | カメラメーカー |
| Model | モデル | カメラのモデル名 |
| Year | 年 | 発売年 |
| image_file | 画像ファイル | カメラ画像へのパス |
| Total megapixels | 総画素数 | 総メガピクセル数 |
| Exposure Compensation | 露出補正 | 利用可能な露出補正範囲 |
| Normal focus range | 通常フォーカス範囲 | 通常のフォーカス距離範囲 |
| Battery | バッテリー | バッテリータイプ |
| Sensor resolution | センサー解像度 | 解像度（ピクセル幅 x 高さ） |
| Crop factor | クロップファクター | センサーのクロップ係数 |
| Sensor type | センサータイプ | 画像センサーの種類（CCD、CMOSなど） |
| Dimensions | 寸法 | 物理的な寸法（mm） |
| Max aperture | 最大絞り値 | 最大絞り値 |
| Min. shutter speed | 最低シャッタースピード | 最低シャッタースピード |
| White balance presets | ホワイトバランスプリセット | ホワイトバランスプリセットの数 |
| Macro focus range | マクロフォーカス範囲 | マクロ撮影の最小フォーカス距離 |
| Optical zoom | 光学ズーム | 光学ズームの有無 |
| USB | USBインターフェース | USBインターフェースのタイプ |
| Weight | 重量 | カメラの重量（g） |
| Max. aperture (35mm equiv.) | 最大絞り値（35mm換算） | 35mm換算の最大絞り値 |
| Focal length (35mm equiv.) | 焦点距離（35mm換算） | 35mm換算の焦点距離範囲 |
| Also known as | 別名 | 代替名またはモデル |
| Aperture priority | 絞り優先 | 絞り優先モードの有無 |
| Max. image resolution | 最大画像解像度 | 最大画像解像度（ピクセル） |
| Max. shutter speed | 最高シャッタースピード | 最高シャッタースピード |
| Storage types | ストレージタイプ | 互換性のあるストレージメディア |
| Effective megapixels | 有効画素数 | 画像キャプチャに使用される有効メガピクセル |
| Megapixels | メガピクセル | マーケティング上のメガピクセル数 |
| Max. video resolution | 最大ビデオ解像度 | 最大ビデオ解像度 |
| Screen size | 画面サイズ | LCDスクリーンサイズ（インチ） |
| Metering | 測光 | 利用可能な測光モード |
| Digital zoom | デジタルズーム | デジタルズームの有無 |
| Shutter priority | シャッター優先 | シャッター優先モードの有無 |
| Sensor size | センサーサイズ | 物理的なセンサーサイズ（mm） |
| Viewfinder | ファインダー | ファインダーのタイプ |
| Screen resolution | 画面解像度 | LCD画面の解像度（ドット） |
| ISO | ISO感度 | 利用可能なISO感度範囲 |

## データ形式

データは2つの形式で提供されています：

1. **CSV**：スプレッドシートアプリケーションやデータ分析ツールに適した単純な表形式
2. **JSON**：ウェブアプリケーションやプログラミングに適した構造化フォーマット

### JSONの例

```json
{
    "Brand": "Canon",
    "Model": "EOS R5 Mark II",
    "Year": "2024",
    "image_file": "data/images/canon_eos-r5-mark-ii.jpg",
    "Total megapixels": "50.3",
    "Exposure Compensation": "\u00b13 EV (in 1/3 EV, 1/2 EV steps)",
    "Normal focus range": null,
    "Battery": "LP-E6P lithium-ion battery",
    "Sensor resolution": "8216 x 5477",
    "Crop factor": "1.0",
    "Sensor type": "CMOS",
    "Dimensions": "138.5 x 101.2 x 93.5 mm",
    "Max aperture": null,
    "Min. shutter speed": "30 sec",
    "White balance presets": "8.0",
    "Macro focus range": null,
    "Optical zoom": null,
    "USB": "USB 3.2 (10 GBit/sec)",
    "Weight": "746 g",
    "Max. aperture (35mm equiv.)": null,
    "Focal length (35mm equiv.)": null,
    "Also known as": null,
    "Aperture priority": "Yes",
    "Max. image resolution": "8192 x 5464",
    "Max. shutter speed": "1/8000 sec",
    "Storage types": "SD/SDHC/SDXC, CFexpress Type B",
    "Effective megapixels": "45.0",
    "Megapixels": null,
    "Max. video resolution": "8192x4320 (60/50/30p/\u200b25p/24p)",
    "Screen size": "3.2\"",
    "Metering": "Multi, Center-weighted, Spot, Partial",
    "Digital zoom": null,
    "Shutter priority": "Yes",
    "Sensor size": "36 x 24 mm",
    "Viewfinder": "Electronic",
    "Screen resolution": "2,100,000 dots",
    "ISO": "Auto, 100-51200 (extends to 50-102400)"
  }
```

## 用途

このデータセットは以下の用途に使用できます：

- カメラ市場分析
- コンピュータビジョン研究
- 機械学習モデルのトレーニング
- カメラ推奨システム
- 教育目的

## データクリーニング

データは以下のようにクリーニングされています：
- 空の列を削除
- 列名を標準化
- ブランドと発売年（降順）でソート
- JSON形式ですべての欠損値をnullに変換

## ライセンス

このデータセットはMITライセンスの下で公開されています。商用および非商用目的での使用が自由です。

## 貢献

データセットの改善への貢献を歓迎します。プルリクエストを提出するか、問題を開いてアイデアを議論してください。

## 謝辞

元の仕様を提供してくれたすべてのカメラメーカーとレビューサイトに感謝します。 
