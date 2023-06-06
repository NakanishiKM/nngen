# 前提条件

Kria KV260

[Xilinx公式イメージUbuntu22.04LTS](https://ubuntu.com/download/amd-xilinx): iot-limerick-kria-classic-desktop-2204-x07-20230302-63.img.xz

[PYNQ環境](https://github.com/Xilinx/Kria-PYNQ.git): mainブランチコミットID0053588

[nngen](https://github.com/sefutsu/nngen/tree/training): trainingブランチコミットIDcc87b93ea

# 再現手順

### 環境構築

**Ubuntu22.04LTS**

[公式の手順](https://www.xilinx.com/products/som/kria/kv260-vision-starter-kit/kv260-getting-started-ubuntu/setting-up-the-sd-card-image.html)に従い、インストールを実行

KV260にマウス、キーボード、ディスプレイを接続し起動する。

ログイン画面が表示されたら、

```
user: ubuntu
pass: ubuntu
```

を入力。初回起動時にパスワードを変更するよう要求されるので任意のパスワードに変更。

ログインできればterminalでIPアドレスを確認。

```sh
$ ip a
```

確認できたIPアドレスを使用してSSH接続。

**PYNQ**

[公式の手順](https://github.com/Xilinx/Kria-PYNQ)に従い、インストールを実行

**nngen**

[公式の手順](https://github.com/NNgen/nngen)に従い、インストールを実行

ブランチをtraining_reproduceにチェックアウト(/nngenでないと見つかりません)

### 実行

```sh
$ cd nngen/training/float_backward
$ sudo -s
root# source /usr/local/share/pynq-venv/bin/active
(pynq-venv)root# python main.py
Using NNgen version 1.3.4.2
Epoch: 1, Cost: 1.937, Accuracy0: 0.980, Accuracy9: 0.583, Accuracy: 0.623
Epoch: 2, Cost: 0.859, Accuracy0: 0.940, Accuracy9: 0.698, Accuracy: 0.722
Epoch: 3, Cost: 0.522, Accuracy0: 0.930, Accuracy9: 0.820, Accuracy: 0.831
Epoch: 4, Cost: 0.392, Accuracy0: 0.920, Accuracy9: 0.884, Accuracy: 0.888
Epoch: 5, Cost: 0.304, Accuracy0: 0.930, Accuracy9: 0.861, Accuracy: 0.868
Elapsed Time: 1358.017 s
```

# 補足

pynq環境に入らないと以下のエラーが発生する。root権限でpynq環境をアクティベートする。

> OSError: Root permissions required.

