# Risk Gate Module - token card UI with dynamic risk scoring
async def token_card_kb_secure(mode: str, mint: str, has_position: bool = False,
           active_limits: list = None, active_buy_limits: list = None,
           *, force: bool = False, hot_only: bool = True) -> InlineKeyboardMarkup:

    """
    - force=True: always return original keyboard (skip gate)
    - hot_only=True: show gate only when token is "hot"
    """

    if force:
        return token_card_kb(mode, mint, has_position, active_limits, active_buy_limits)
    
    risk = await _risk_cached(mint)

    if hot_only:
         gate = bool(risk.get("hot_gate"))
    else:
        gate = (risk["risk_score"] > RUG_THRESHOLD)


    if not gate:
        return token_card_kb(mode, mint, has_position, active_limits, active_buy_limits)
        

    hot_lines = " • ".join(risk.get("hot_reasons", [])[:3]) or "High short-term risk"
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "⚠️ I Understand the Risk — Continue",
                    callback_data=f"confirm_buy|{mint}",
                )
            ],
            [
                InlineKeyboardButton(
                    "📈 Chart",
                    url=f"https://dexscreener.com/solana/{mint}",
                )
            ],
            [
                InlineKeyboardButton(
                    "🧾 Solscan",
                    url=f"https://solscan.io/token/{mint}",
                )
            ],
            [
                InlineKeyboardButton(
                    "ℹ️ Why?",
                    callback_data=f"hot_info|{mint}",
                )
            ],
        ]
    )
