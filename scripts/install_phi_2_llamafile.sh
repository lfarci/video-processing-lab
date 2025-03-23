wget https://huggingface.co/jartine/phi-2-llamafile/resolve/main/phi-2.Q4_K_M.llamafile
chmod +x phi-2.Q4_K_M.llamafile

# Start the model server. Listens at http://localhost:8080 by default.
./phi-2.Q4_K_M.llamafile --server --nobrowser