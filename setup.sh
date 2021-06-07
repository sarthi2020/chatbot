mkdir -p ~/.streamlit/
echo "\
[server]\n\
<<<<<<< HEAD
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
=======
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml
>>>>>>> 125d51d40385165a74b23e5257f1500d561d0a08
