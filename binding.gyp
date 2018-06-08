{
    "targets": [
        {
            "target_name": "equihashverify",
            "dependencies": [
                "libequi",
            ],
            "sources": [
                "equihashverify.cc",
            ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")"
            ],
            "defines": [
            ],
            "cflags_cc": [
                "-std=c++11",
                "-Wl,--whole-archive",
                "-fPIC",
            ],
            "link_settings": {
                "libraries": [
                    "-Wl,-rpath,./build/Release/",
                ]
            },
        },
        {
            "target_name": "libequi",
            "type": "<(library)",
            "dependencies": [
            ],
            "sources": [
                "src/equi/equi.cpp"
            ],
            "include_dirs": [
            ],
            "defines": [
            ],
            "cflags_cc": [
                "-std=c++11",
                "-Wl,--whole-archive",
                "-fPIC",
                "-D_GNU_SOURCE"
            ],
            "link_settings": {
                "libraries": [
                    "-lsodium"
                ],
            },
        }
    ]
}

