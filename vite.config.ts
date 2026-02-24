import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

import { viteStaticCopy } from 'vite-plugin-static-copy';

export default defineConfig({
	plugins: [
		sveltekit(),
		viteStaticCopy({
			targets: [
				{
					src: 'node_modules/onnxruntime-web/dist/*.jsep.*',

					dest: 'wasm'
				}
			]
		})
	],
	server: {
		proxy: {
			'/api': {
				target: 'http://127.0.0.1:8080',
				changeOrigin: true
			},
			'/ollama': {
				target: 'http://127.0.0.1:8080',
				changeOrigin: true
			},
			'/openai': {
				target: 'http://127.0.0.1:8080',
				changeOrigin: true
			},
			'/images': {
				target: 'http://127.0.0.1:8080',
				changeOrigin: true
			},
			'/uploads': {
				target: 'http://127.0.0.1:8080',
				changeOrigin: true
			},
			'/ws': {
				target: 'ws://127.0.0.1:8080',
				changeOrigin: true,
				ws: true,
				rewrite: (path) => path.replace(/^\/ws/, '/ws')
			}
		}
	},
	define: {
		APP_VERSION: JSON.stringify(process.env.npm_package_version),
		APP_BUILD_HASH: JSON.stringify(process.env.APP_BUILD_HASH || 'dev-build'),
		'process.env.WEBUI_BASE_URL': JSON.stringify(process.env.WEBUI_BASE_URL)
	},
	build: {
		sourcemap: false,
		chunkSizeWarningLimit: 20000,
		cssCodeSplit: false,
		rollupOptions: {
			output: {
				compact: true,
				entryFileNames: 'assets/[name]-[hash].js',
				chunkFileNames: 'assets/[name]-[hash].js',
				assetFileNames: 'assets/[name]-[hash].[ext]'
			},
			external: []
		}
	},
	worker: {
		format: 'es'
	},
	esbuild: {
		pure: process.env.ENV === 'dev' ? [] : ['console.log', 'console.debug', 'console.error'],
		treeShaking: true
	}
});
