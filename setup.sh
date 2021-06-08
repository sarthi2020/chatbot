mkdir -p ~/.streamlit/
echo "\
[server]\n\
<<<<<<< HEAD
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml

