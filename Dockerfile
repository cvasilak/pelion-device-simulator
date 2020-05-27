FROM node:12.14

ENV PATH="/emsdk:/emsdk/emscripten/tag-1.38.21:${PATH}"
ENV EMSDK="/emsdk"
ENV EM_CONFIG="/root/.emscripten"
ENV EMSCRIPTEN="/emsdk/emscripten/tag-1.38.21"
ENV EMSCRIPTEN_NATIVE_OPTIMIZER="/emsdk/emscripten/tag-1.38.21_64bit_optimizer/optimizer"

RUN apt-get update -qq && apt-get -qqy install \
        cmake git python-dev python-pip && \
    pip install mbed-cli==1.10.2 mercurial && \
    git clone https://github.com/emscripten-core/emsdk && cd emsdk && git checkout 1.39.8 && cd ..

RUN emsdk/emsdk install fastcomp-clang-e1.38.21-64bit && \
    emsdk/emsdk activate fastcomp-clang-e1.38.21-64bit && \
    emsdk/emsdk install emscripten-tag-1.38.21-64bit && \
    emsdk/emsdk activate emscripten-tag-1.38.21-64bit

ADD internal /app
WORKDIR /app
RUN npm install && npm run build-demos -i demos

ADD peliondm/example /app/demos/peliondm
ADD peliondm/build-pelion-and-launch.js /app

EXPOSE 7829

#CMD ["node", "server.js"]
CMD ["npm", "run", "build-pelion-and-launch"]
