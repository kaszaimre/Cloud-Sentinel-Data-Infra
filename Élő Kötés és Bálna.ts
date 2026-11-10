// ActiveTradeFeed.tsx - Élő Kötés és Bálna-Figyelő Panel
import React, { useEffect, useState } from 'react';

interface TradeLog {
    timestamp: string;
    ticker: string;
    type: 'BUY' | 'SELL' | 'SL' | 'TP';
    price: number;
    agentName: string;
    profit?: string;
}

export const ActiveTradeFeed: React.FC = () => {
    const [trades, setTrades] = useState<TradeLog[]>([]);

    // SzalonnaNet WebSocket kapcsolat az 5000+ futó kód élő eseményeihez
    useEffect(() => {
        const ws = new WebSocket('ws://localhost:8080/sigma-orders');
        ws.onmessage = (event) => {
            const newTrade = JSON.parse(event.data);
            setTrades(prev => [newTrade, ...prev.slice(0, 4)]); // Csak az utolsó 5 trade-et tartja meg
        };
        return () => ws.close();
    }, []);

    return (
        <div className="p-4 bg-slate-900 border border-purple-900 rounded-lg">
            <h3 className="text-sm font-bold text-cyan-400 mb-3 flex items-center">
                <span className="animate-ping inline-block w-2 h-2 mr-2 rounded-full bg-emerald-400"></span>
                SIGMA TRADING EXECUTION FEED (ÉLŐ)
            </h3>
            <div className="space-y-2">
                {trades.map((trade, idx) => (
                    <div key={idx} className="flex justify-between items-center text-xs p-2 bg-slate-950 rounded border border-slate-800">
                        <span className="text-slate-500">{trade.timestamp}</span>
                        <span className="font-bold text-white">{trade.ticker}</span>
                        <span className={`font-bold ${trade.type.includes('BUY') ? 'text-emerald-400' : 'text-rose-500'}`}>
                            {trade.type}
                        </span>
                        <span className="text-cyan-300">${trade.price}</span>
                        <span className="text-purple-400 text-[10px] font-mono">{trade.agentName}</span>
                    </div>
                ))}
            </div>
        </div>
    );
};
