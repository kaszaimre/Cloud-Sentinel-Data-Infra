package com.borsodibrigad.phoenixmaster;

import android.annotation.SuppressLint;
import android.app.Activity;
import android.os.Bundle;
import android.view.Window;
import android.view.WindowManager;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class MainActivity extends Activity {

    private WebView mWebView;

    @Override
    @SuppressLint("SetJavaScriptEnabled")
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Kognitív zaj csökkentése: Teljes képernyős katonai HUD mód aktiválása
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, 
                            WindowManager.LayoutParams.FLAG_FULLSCREEN);

        mWebView = new WebView(this);
        WebSettings webSettings = mWebView.getSettings();
        
        // Biztonsági hardening protokollok
        webSettings.setJavaScriptEnabled(true); // JavaScript engedélyezése az inline mátrix-frissítéshez
        webSettings.setAllowFileAccess(true);
        webSettings.setAllowFileAccessFromFileURLs(true);
        webSettings.setAllowUniversalAccessFromFileURLs(true);
        
        // Cache kisöprése minden indításkor az Oracle Szabálykönyv 9. pontja szerint
        webSettings.setCacheMode(WebSettings.LOAD_NO_CACHE);

        mWebView.setWebViewClient(new WebViewClient());

        // A helyi hardverre égetett, megsemmisíthetetlen forrásfájl betöltése
        mWebView.loadUrl("file:///android_asset/www/index.html");
        setContentView(mWebView);
    }

    @Override
    public void onBackPressed() {
        // Védelmi gyűrű: Letiltjuk a véletlen kilépést gépelés vagy vezetés közben
        if (mWebView.canGoBack()) {
            mWebView.goBack();
        } else {
            // Egyedi parancsnoki döntés: nem lép ki a szoftver azonnal zajra
            super.onBackPressed();
        }
    }
}
