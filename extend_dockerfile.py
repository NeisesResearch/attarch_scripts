lines_to_append = """
RUN curl -L https://github.com/CakeML/cakeml/releases/download/v2076/cake-x64-32.tar.gz > cake-x64-32.tar.gz \\
    && tar -xvzf cake-x64-32.tar.gz && cd cake-x64-32 && make cake \\
    && mv cake /usr/bin/cake32

RUN curl -L https://github.com/CakeML/cakeml/releases/download/v2076/cake-x64-64.tar.gz > cake-x64-64.tar.gz \\
    && tar -xvzf cake-x64-64.tar.gz && cd cake-x64-64 && make cake \\
    && mv cake /usr/bin/cake64
"""

filename = "seL4-CAmkES-L4v-dockerfiles/dockerfiles/extras.Dockerfile"

with open(filename, 'a') as file:
    file.write(lines_to_append)

