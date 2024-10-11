package com.example.platform.common;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * 自定义返回类
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
public class result {
    private String code;
    private String msg;
    private Object data;
    public static result success(Object data) {
        return new result(constants.code_200,"",data);
    }
    public static result success() {
        return new result(constants.code_200,"",null);
    }
    public static result error(String code, String msg) {
        return new result(code,msg,null);
    }
//    public static result error() {
//        return new result(constants.code_500,"系统错误",null);
//    }
}
