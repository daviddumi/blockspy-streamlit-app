import streamlit as st
from streamlit_option_menu import option_menu
from data_engine import style_24h_change, get_token_data
st.set_page_config(
    layout="wide",
    page_icon="/Users/ouris/PycharmProjects/Blockspy/favicon.png"
)

selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Shrap 🧠", "Prime 🧠", "Domi 🧠", "w3ULL 🧠","sync 🧠", "About", "Donate"],  # required
            icons=["house", "activity", "activity", "activity", "activity", "activity", "file-person", "wallet"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#595959"},
                "icon": {"color": "#00cc7a", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "#999999"},
            },
        )

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

if selected == "Home":
    st.title(f"What is this and why?")
    st.markdown("""
            Crypto is full of insider trading, as we all know. This is like a hedgefund manager calling another hedgefund manager to short a stock,
            except this data is now all on chain. We don't know their goverment names, but we know their 0x address!
            
            So like many of you, I saw Axie Infinity rise from .10 to 150 last cycle. I thought to myself WHO TF was buying it that low, they made millions! 
            
            So I figured it out.
            
            Now that the market is heating up again, we can get some fresh data. Those old wallets might me decomissioned, or lost. But we have several coins
            that pumped recently to track.
            
            So the 🧠 wallets (I call them wrinkles) are all of the wallets that purchased more of a token than they sold, in a given timeframe.
            
            I have also removed bot wallets like jaredfromsubway.eth, so the list of wallets is quite clean actually.
            
            I based the timeframe off of recent pumps, going from essentially 0 to 1, and I included the red days after an initial pump to include those who were waiting for a better entry. 
            
            You can see here on the $domi chart, the timeframe that I based wallet purchases off of. 
        """)
    image_path = '/Users/ouris/PycharmProjects/Blockspy/example_chart.png'
    st.image(image_path, width=400, caption='Domi Purchase Timeframe')
    st.markdown("""
            Once I had the list of wallets I then track all of their purchases and sells in the last day, and look at the tokens that were net purchased today by those wallets.
            
            Then the token data is enriched from the dexscreener.com api, so we can get some price and fdv numbers.
            
            This runs daily and if you want it to run hourly please consider donating. Data isnt free.
     """)
if selected == "Shrap 🧠":
    st.title(f"{selected} tokens purchased in the last day")
    df = get_token_data("shrap")
    st.dataframe(df, use_container_width=True, height=500)
if selected == "Prime 🧠":
    st.title(f"{selected} tokens purchased in the last day")
    df = get_token_data("prime")
    st.dataframe(df, use_container_width=True, height=500)
if selected == "Domi 🧠":
    st.title(f"{selected} tokens purchased in the last day")
    df = get_token_data("domi")
    st.dataframe(df, use_container_width=True, height=500)
if selected == "w3ULL 🧠":
    st.title(f"{selected} tokens purchased in the last day")
    df = get_token_data("w3ull")
    st.dataframe(df, use_container_width=True, height=500)
if selected == "Sync 🧠":
    st.title(f"{selected} tokens purchased in the last day")
    df = get_token_data("sync")
    st.dataframe(df, use_container_width=True, height=500)
if selected == "About":
    st.title(f"{selected}")
    st.markdown("""
        I am just a guy who fell in love with crypto.  At some point down the crypto research rabbit hole,
        you start reading whitepapers and eventually reading smart contracts to see if you are getting scammed.
        
        That led me start learning how to code, and the rest is history. There should be a better version of this site soon!
        
        You can find me @pellegrypto on twitter, or x whatever lol.
    """)
if selected == "Donate":
    st.markdown("""
        API calls arent free! If you want me to add wallet holdings, nft trades, nft holdings, new coins, etc.
        then feel free to donate. 
        
        BTC: 37R5GFVUSRd8HGM9nfV2bUfb89v2G6YDq9
        
        ETH(EVM): 0x1D6e993028eC4FDDDe3171F1EC9251CC19c71Aec (mintaddict.eth)
        
        SOL: 9kuQiLazuPU92ctaBLGBb3eUqs3PKgfGbnubrgsGFwMK (mintaddict.sol)
    """)