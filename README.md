# Solana Trading Bot
A live Solana trading bot built and deployed independently via Telegram.

## What it does
- Real on-chain trade execution via Telegram
- Automated TP/SL, MEV Protection, Priority Fees
- Live SOL price feed and price alerts
- PnL tracking per position
- Dual Wallet architecture - bot generated or external wallet
- Transfer functionality

  <p align="center">
  <img src="Preview.png" width="400" alt="SkiltexBot interface">
  <br>
  <em>Live bot interface — deployed and operational</em>
</p>

## Features
- Automated risk scoring and rug pull detection
- Low fee model
- Whitelist address security

## Tech Stack
- Python
-  Solana RPC
-  Jupiter v1 Lite API
-  Telegram Bot API
-  Hetzner Cloud Infrastructure
-  Ubuntu 22.04
-  Webhook
-  DexScreener
-  Solscan
-  Mev Protection(Jito)
  
## Architecture
Non-custodial. Users connect external wallets or use a bot-generated wallet. Zero platform access to private keys at any point.
Deployed on Hetzner Cloud Infrastructure

## Status
Live and Operational - 2025 to Present

## Roadmap 
- Phase 1: Solana trading - live
- Phase 2: Ethereum network integration - upcoming
- Phase 3: Web Platform with KOL tracking and copy trading and cross-chain bridge - in development at skiltex.io
