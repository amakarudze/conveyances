const path = require('path')
const { VueLoaderPlugin } = require('vue-loader')
const BundleTracker = require('webpack-bundle-tracker');
const webpack = require("webpack");

module.exports = (env = {}) => {
  return {
    context: __dirname,
    mode: env.prod ? 'production' : 'development',
    devtool: env.prod ? false : 'source-map',
    entry: {
      app: './src/main.js',
    },
    output: {
      path: path.resolve('./dist'),
      filename: "[name]-[fullhash].js",
      chunkFilename: '[name].bundle.js',
    },
    module: {
      rules: [
        {
          test: /\.vue$/,
          use: 'vue-loader'
        },
        {
          test: /\.ts$/,
          loader: 'ts-loader',
          options: {
            appendTsSuffixTo: [/\.vue$/],
          },
        },
        {
          test: /\.js$/,
          exclude: /node_modules/,
          use: {
            loader: "babel-loader",
          },
        },
        {
          test: /\.css$/,
          exclude: /node_modules/,
          use: ["style-loader", "css-loader",],
        },
        {
          test: /\.(png|svg|jpe?g|gif)$/i,
          loader: "file-loader",
          options: {
            outputPath: "assets",
          },
        },
      ],
    },
    resolve: {
      modules: ['node_modules'],
      extensions: ['.ts', '.js', '.vue', '.json'],
      alias: {
        'vue': '@vue/runtime-dom',
        "@": path.resolve("./src"),
      },
    },
    plugins: [
      new VueLoaderPlugin(),
      new BundleTracker({
        filename: './webpack-stats.json',
        publicPath: 'http://127.0.0.1:8080/',
      }),
      new webpack.LoaderOptionsPlugin({
        // test: /\.xxx$/, // may apply this only for some modules
        options: {
          indexPath: "../../templates/index.html",
          outputDir: "./dist/",
        },
      }),
    ],
    devServer: {
      headers: {
        "Access-Control-Allow-Origin":"\*"
      },
      host: '127.0.0.1',
      port: 8080,
      hot: true,
      https: false,
      static: '__STATIC__',
    },
  };
}