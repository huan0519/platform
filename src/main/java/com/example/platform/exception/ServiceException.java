package com.example.platform.exception;

import lombok.Getter;

@Getter
public class ServiceException extends RuntimeException {
    private String code;
    public ServiceException(String code, String message) {
        super(message);
        this.code = code;
    }
}
